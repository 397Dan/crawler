#usr/bin/python
#coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

try:
    # 切换到id为iframeResult的窗口内
    driver.switch_to.frame('iframeResult')

    #源位置
    draggable=driver.find_element_by_id('draggable')

    #目的位置
    droppable=driver.find_element_by_id('droppable')
    # 调用ActionChains，必须把驱动对象进去
    actions=ActionChains(driver)

    # #方式一
    # # 瞬间把源图片位置秒移到目标图片位置
    # actions.drag_and_drop(draggable,droppable)
    # #执行编辑好的行为
    # actions.perform()
    # time.sleep(5)

    #方式二
    source=draggable.location['x']
    target=droppable.location['x']
    print(source,target)

    distance=target-source
    print(distance)

    ActionChains(driver).click_and_hold(draggable).perform()
    s=0
    while s<distance:
        ActionChains(driver).move_by_offset(xoffset=2,yoffset=0).perform()
        s+=2

    ActionChains(driver).release().perform()
    time.sleep(10)

finally:
    driver.close()