import schedule
import pywhatkit




from datetime import datetime , time , timedelta
import time as tm
def job() :
    pywhatkit.sendwhatmsg("+91991069302", "reached!", 15, 10)








schedule.every().day.at("15:10").do(job)



while True :
    schedule.run_pending()
    tm.sleep(1)

