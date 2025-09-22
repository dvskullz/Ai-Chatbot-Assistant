import requests
import speedtest

def run_speedtest():
    """
    Run an internet speed test and return results as a string.
    """
    try:
        st = speedtest.Speedtest()
        st.get_servers([])
        downlink_bps = st.download()
        uplink_bps = st.upload()
        ping = st.results.ping
        up_mbps = uplink_bps / 1_000_000
        down_mbps = downlink_bps / 1_000_000
        return (f"Speedtest results:\n"
                f"Ping: {ping:.0f} ms\n"
                f"Upload: {up_mbps:.2f} Mbps\n"
                f"Download: {down_mbps:.2f} Mbps")
    except Exception as e:
        return f"Sorry, I couldn't run a speedtest. {e}"

def internet_availability():
    """
    Check if the internet is available by pinging Google.
    """
    try:
        requests.get("https://www.google.com", timeout=3)
        return "The internet connection is OK."
    except Exception:
        return "The internet is down for now."