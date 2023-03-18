from plyer import notification
import time

if __name__=='__main__':
    while True:
        notification.notify(
            title="Take Rest",
            message="Rest is very important for maintaing good health",
            timeout=6)
        time.sleep(10)
