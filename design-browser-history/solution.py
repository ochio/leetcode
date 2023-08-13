class BrowserHistory:
    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.urls = self.urls[: self.i + 1] + [url]
        self.i = len(self.urls) - 1

    def back(self, steps: int) -> str:
        self.i -= steps
        self.i = max(0, self.i)
        return self.urls[self.i]

    def forward(self, steps: int) -> str:
        self.i += steps
        self.i = min(len(self.urls) - 1, self.i)
        return self.urls[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
