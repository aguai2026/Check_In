from util import *

# username = sys.argv[1] # 登录账号
# password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

driver = None

@retry(stop_max_attempt_number=5)
def freedoor():
    try:
        driver = get_web_driver()
        driver.get("https://freedoor.vip/auth/login")
        try:
            # 1. 强制等待最多 20 秒，直到 email 输入框出现
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='email']"))
            )
            email_input.send_keys("2038386045@qq.com")
        except Exception as e:
            # 2. 如果找不到，立刻保存一张截图，并打印当前网页的标题
            print("=== 错误：找不到邮箱输入框，已截图 ===")
            driver.save_screenshot("error_screenshot.png")
            print(f"当前网页标题: {driver.title}")
            print(f"当前网页网址: {driver.current_url}")
            # 打印当前页面的源码长度，如果非常短，说明被拦截了
            print(f"当前网页源码长度: {len(driver.page_source)}")
            raise e
        

        
        driver.find_element(By.XPATH, "//*[@id='email']").send_keys("2038386045@qq.com")
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys("Fdv.2026")
        driver.find_element(By.XPATH, "//*[@id='login-btn']").click()


        driver.find_element(By.XPATH, "//*[@id='check-in']").click()
        print('freedoor签到成功')
    except:
        raise
    finally:
        if driver is not None:
            driver.quit()
        

if __name__ == '__main__':
    freedoor()
