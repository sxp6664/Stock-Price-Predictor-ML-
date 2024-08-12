def generate_features(data):
    """Generate features for the model."""
    data['SMA_20'] = data['Close'].rolling(window=20).mean()  # Simple Moving Average
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['Return'] = data['Close'].pct_change()
    return data
