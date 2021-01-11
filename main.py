import sys
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from jd_spider_requests import JdSeckill

def seckill():
    jd_seckill = JdSeckill()
    jd_seckill.seckill_by_proc_pool()

def login_checker():
    jd_seckill = JdSeckill()
    jd_seckill.loginChecker()

if __name__ == '__main__':
    a = """

    .__       .__                   .___.__                
    |__| ____ |  |   ____  __ __  __| _/|__| ____    ____  
    |  |/ ___\|  |  /  _ \|  |  \/ __ | |  |/    \  / ___\ 
    |  \  \___|  |_(  <_> )  |  / /_/ | |  |   |  \/ /_/  >
    |__|\___  >____/\____/|____/\____ | |__|___|  /\___  / 
            \/                       \/         \//_____/                                                                                                                                                
                                               
功能列表：                                                                                
 1.预约商品
 2.秒杀抢购商品
    """
    print(a)
    # 记录当前时间
    login_checker()
    scheduler = BlockingScheduler()
    # 添加茅台任务
    scheduler.add_job(seckill , "cron", day='*', hour='09', minute='58')
    scheduler.add_job(login_checker, "cron", day='*', hour='09', minute='50')
    scheduler.start()

    # jd_seckill = JdSeckill()
    # jd_seckill.seckill_by_proc_pool()


    # choice_function = input('请选择:')
    # if choice_function == '1':
    #     jd_seckill.reserve()
    # elif choice_function == '2':
    #     jd_seckill.seckill_by_proc_pool()
    # else:
    #     print('没有此功能')
    #     sys.exit(1)

