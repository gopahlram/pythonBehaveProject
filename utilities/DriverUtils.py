class DriverUtils:

    def __init__(self, driver):
        self.driver = driver

    def get_parent_windowHandle(self):
        return self.driver.current_window_handle

    def switch_to_window(self, handles, parent_handle):
        for handle in handles:
            if handle not in parent_handle:
                self.driver.switch_to.window(handle)

    def get_all_windows(self):
        return self.driver.window_handles
