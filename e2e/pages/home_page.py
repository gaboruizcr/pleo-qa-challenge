
from e2e.pages.base_page import BasePage

# page locators
btn_submit = '#submit'
h1_title= 'h1'
h2_title= 'h2'
lbl_result = "#result"
lbl_message = '.result-message'
txt_money = "#money"

# page actions
class HomePage(BasePage):
    def __init__(self, page, base_url:str) -> None:
        BasePage.__init__(self, page, base_url)

    def go_to(self) -> None:
        BasePage.go_to(self, f'{self.base_url}/')

    def format_text(self, money_text: str) -> None:
        self.page.type(txt_money, money_text)
        self.click_submit()
    
    def get_title(self) -> str:
        return self.page.title()

    # single element attributes/actions
    def click_submit(self) -> None:
        self.page.click(btn_submit)

    def get_title_text(self) -> str:
        return self.page.inner_text(h1_title)
    
    def get_sub_title_text(self) -> str:
        return self.page.inner_text(h2_title)

    def get_message_text(self) -> str:
        return self.page.inner_text(lbl_message)

    def get_submit_type(self) -> str:
        return self.page.get_attribute(btn_submit, "type")

    def get_result_text(self) -> str:
        return self.page.inner_text(lbl_result)

    def get_submit_text(self) -> str:
        return self.page.inner_text(btn_submit)

        

