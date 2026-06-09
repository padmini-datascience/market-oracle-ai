import requests

def get_options_data():

    print("OPTIONS FUNCTION CALLED")

    try:

        url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        session = requests.Session()

        session.get(
            "https://www.nseindia.com",
            headers=headers,
            timeout=10
        )

        response = session.get(
            url,
            headers=headers,
            timeout=10
        )
        print("FINAL URL:", response.url)
        print("STATUS CODE:", response.status_code)
        print("CONTENT TYPE:", response.headers.get("content-type"))
        print("TEXT SAMPLE:", response.text[:300])


        data = response.json()

        records = data["records"]["data"]

        call_oi = 0
        put_oi = 0

        for row in records:

            if "CE" in row:
                call_oi += row["CE"]["openInterest"]

            if "PE" in row:
                put_oi += row["PE"]["openInterest"]

        if call_oi > 0:
            pcr = round(put_oi / call_oi, 2)
        else:
            pcr = 0

        if pcr > 1:
            pcr_status = "BULLISH"
        elif pcr < 0.7:
            pcr_status = "BEARISH"
        else:
            pcr_status = "NEUTRAL"

        return {
        "PCR": pcr,
        "PCR_Status": pcr_status,
        "Call_OI": call_oi,
        "Put_OI": put_oi,
        "STATUS_CODE": response.status_code,
        "CONTENT_TYPE": response.headers.get("content-type")
    }
    
    except Exception as e:

       return {
    "PCR": 0,
    "PCR_Status": "DUMMY",
    "Call_OI": 100000,
    "Put_OI": 120000
    } 