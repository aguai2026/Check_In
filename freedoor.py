from util import *

# username = sys.argv[1] # 登录账号
# password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

@retry(stop_max_attempt_number=5)
def freedoor():
    try:
        driver = get_web_driver()
        driver.get("https://freedoor.vip/auth/login")
        driver.find_element(By.xpath, "//*[@id='email']").send_keys("2038386045@qq.com")
        driver.find_element(By.xpath, "//*[@id='password']").send_keys("Fdv.2026")
        driver.find_element(By.xpath, "//*[@id='login-btn']").click()


        driver.find_element(By.xpath, "//*[@id='check-in']").click()
        print('freedoor签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    freedoor()
