import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class StockAnalyzer:
    def __init__(self, symbol, period='1y'):
        self.symbol = symbol
        self.period = period
        self.data = None
        
    def fetch_data(self):
        """Fetch stock data from Yahoo Finance"""
        try:
            ticker = yf.Ticker(self.symbol)
            self.data = ticker.history(period=self.period)
            if self.data.empty:
                raise ValueError(f"No data found for symbol {self.symbol}")
            print(f"Successfully fetched {len(self.data)} days of data for {self.symbol}")
        except Exception as e:
            print(f"Error fetching data: {e}")
            return False
        return True
    
    def calculate_technical_indicators(self):
        """Calculate various technical indicators"""
        if self.data is None:
            print("No data available. Please fetch data first.")
            return
        
     
        self.data['SMA_20'] = self.data['Close'].rolling(window=20).mean()
        self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()
        self.data['EMA_12'] = self.data['Close'].ewm(span=12).mean()
        self.data['EMA_26'] = self.data['Close'].ewm(span=26).mean()
        
      
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))
        
        self.data['MACD'] = self.data['EMA_12'] - self.data['EMA_26']
        self.data['MACD_Signal'] = self.data['MACD'].ewm(span=9).mean()
        self.data['MACD_Histogram'] = self.data['MACD'] - self.data['MACD_Signal']
        
      
        self.data['BB_Middle'] = self.data['Close'].rolling(window=20).mean()
        bb_std = self.data['Close'].rolling(window=20).std()
        self.data['BB_Upper'] = self.data['BB_Middle'] + (bb_std * 2)
        self.data['BB_Lower'] = self.data['BB_Middle'] - (bb_std * 2)
        
       
        self.data['Volume_SMA'] = self.data['Volume'].rolling(window=20).mean()
        
        print("Technical indicators calculated successfully!")
    
    def calculate_performance_metrics(self):
        """Calculate performance metrics"""
        if self.data is None:
            return {}
        
        # Basic metrics
        current_price = self.data['Close'].iloc[-1]
        initial_price = self.data['Close'].iloc[0]
        total_return = ((current_price - initial_price) / initial_price) * 100
        
        # Volatility (annualized)
        returns = self.data['Close'].pct_change().dropna()
        volatility = returns.std() * np.sqrt(252) * 100
        
        # Sharpe ratio (assuming risk-free rate of 2%)
        risk_free_rate = 0.02
        excess_returns = returns.mean() * 252 - risk_free_rate
        sharpe_ratio = excess_returns / (returns.std() * np.sqrt(252))
        
        # Maximum drawdown
        cumulative = (1 + returns).cumprod()
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / running_max
        max_drawdown = drawdown.min() * 100
        
        # Additional metrics
        avg_volume = self.data['Volume'].mean()
        price_range = ((self.data['High'].max() - self.data['Low'].min()) / self.data['Close'].iloc[0]) * 100
        
        return {
            'Current_Price': current_price,
            'Total_Return': total_return,
            'Volatility': volatility,
            'Sharpe_Ratio': sharpe_ratio,
            'Max_Drawdown': max_drawdown,
            'Avg_Volume': avg_volume,
            'Price_Range': price_range,
            'Data_Points': len(self.data)
        }
    
    def plot_price_analysis(self, figsize=(16, 12)):
        """Create comprehensive price analysis plot"""
        if self.data is None:
            print("No data available. Please fetch data first.")
            return
        
        fig, axes = plt.subplots(4, 1, figsize=figsize)
        fig.suptitle(f'{self.symbol} - Comprehensive Analysis', fontsize=16, fontweight='bold')
        
        # Price chart with moving averages and Bollinger Bands
        ax1 = axes[0]
        ax1.plot(self.data.index, self.data['Close'], label='Close Price', linewidth=2, color='#1f77b4')
        ax1.plot(self.data.index, self.data['SMA_20'], label='SMA 20', alpha=0.7, color='orange')
        ax1.plot(self.data.index, self.data['SMA_50'], label='SMA 50', alpha=0.7, color='red')
        ax1.fill_between(self.data.index, self.data['BB_Upper'], self.data['BB_Lower'], 
                        alpha=0.2, color='gray', label='Bollinger Bands')
        ax1.set_title('Price Chart with Moving Averages and Bollinger Bands')
        ax1.set_ylabel('Price ($)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # RSI
        ax2 = axes[1]
        ax2.plot(self.data.index, self.data['RSI'], color='purple', linewidth=2)
        ax2.axhline(y=70, color='r', linestyle='--', alpha=0.7, label='Overbought (70)')
        ax2.axhline(y=30, color='g', linestyle='--', alpha=0.7, label='Oversold (30)')
        ax2.set_title('Relative Strength Index (RSI)')
        ax2.set_ylabel('RSI')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # MACD
        ax3 = axes[2]
        ax3.plot(self.data.index, self.data['MACD'], label='MACD', color='blue')
        ax3.plot(self.data.index, self.data['MACD_Signal'], label='Signal', color='red')
        ax3.bar(self.data.index, self.data['MACD_Histogram'], label='Histogram', alpha=0.6, color='gray')
        ax3.set_title('MACD (Moving Average Convergence Divergence)')
        ax3.set_ylabel('MACD')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # Volume
        ax4 = axes[3]
        ax4.bar(self.data.index, self.data['Volume'], alpha=0.6, color='lightblue', label='Volume')
        ax4.plot(self.data.index, self.data['Volume_SMA'], color='red', linewidth=2, label='Volume SMA')
        ax4.set_title('Volume Analysis')
        ax4.set_ylabel('Volume')
        ax4.set_xlabel('Date')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()

def analyze_multiple_stocks(symbols, period='1y'):
    """Analyze multiple stocks and return comparison data"""
    results = []
    
    for symbol in symbols:
        try:
            analyzer = StockAnalyzer(symbol, period)
            if analyzer.fetch_data():
                analyzer.calculate_technical_indicators()
                metrics = analyzer.calculate_performance_metrics()
                metrics['Symbol'] = symbol
                results.append(metrics)
                print(f"✓ Analyzed {symbol}")
            else:
                print(f"✗ Failed to analyze {symbol}")
        except Exception as e:
            print(f"✗ Error analyzing {symbol}: {e}")
    
    return pd.DataFrame(results).set_index('Symbol')

# Example usage
if __name__ == "__main__":
    # Single stock analysis
    aapl = StockAnalyzer('AAPL', period='1y')
    aapl.fetch_data()
    aapl.calculate_technical_indicators()
    aapl.plot_price_analysis()
    
    # Performance metrics
    metrics = aapl.calculate_performance_metrics()
    print("\nPerformance Metrics:")
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")
