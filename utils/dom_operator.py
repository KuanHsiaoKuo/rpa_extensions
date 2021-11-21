from selenium import webdriver


class DOMOperator:
    @classmethod
    def add_names(cls, driver: webdriver, xpath_names: dict):
        """
        一般不会给元素添加name，所以这里进行额外添加
        :param driver:
        :param xpath_tags:
        :return:
        """
        for name, xpath in xpath_names.items():
            add_name_js = f"document.evaluate('{xpath}', document).iterateNext().setAttribute('rpa-name', '{name}')"
            driver.execute_script(add_name_js)
            # driver.execute_async_script(add_name_js)
            print(name, xpath)

    @classmethod
    def get_target_elements(cls, driver: webdriver, xpath_names: dict):
        target_elements = {}
        for name, xpath in xpath_names.items():
            # 只需要加return， selenium就可以获取js返回的执行结果
            query_ele_js = f'return document.querySelector("[rpa-name={name}]")'
            target_elements[name] = driver.execute_script(query_ele_js)
            # driver.execute_async_script(add_name_js)
        return target_elements
