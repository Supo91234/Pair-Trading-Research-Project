import yfinance as yf
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

# Download stock data
start_date = "2023-01-03"
end_date = "2025-06-20"

amd = yf.download("AMD", start=start_date, end=end_date)["Close"]
nvda = yf.download("NVDA", start=start_date, end=end_date)["Close"]

# Merge and drop missing values
data = (
    amd.rename("AMD")
    .to_frame()
    .join(nvda.rename("NVDA"), how="inner")
    .dropna()
)

# Take natural logs
data["ln_AMD"] = np.log(data["AMD"])
data["ln_NVDA"] = np.log(data["NVDA"])

# Linear regression: ln(AMD) ~ ln(NVDA)
X = sm.add_constant(data["ln_NVDA"])
model = sm.OLS(data["ln_AMD"], X).fit()
residuals = model.resid

# Augmented Dickey-Fuller test on residuals
adf_result = adfuller(residuals)

print(f"ADF Statistic: {adf_result[0]}")
print(f"p-value: {adf_result[1]}")
print("Critical Values:", adf_result[4])

if adf_result[1] < 0.05:
    print("✅ The stocks are likely cointegrated (reject null hypothesis)")
else:
    print("❌ No cointegration found (fail to reject null hypothesis)")
