from fastapi import HTTPException


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 20, p: int = None, p_size: int = 5):
        self.q = q
        self.skip = skip
        self.limit = limit
        # page option
        self.p = p
        self.p_size = p_size
        self.checkPageNumParam()

    def checkPageNumParam(self):
        """
        if param 'p' exists then convert to corresponding params 'skip' and 'limit'
        :return: void
        """
        if self.p:
            if self.p < 1:
                raise HTTPException(status_code=400, detail="Invalid Page Num")
            if self.p_size < 1 or self.p_size > 50:
                raise HTTPException(status_code=400, detail="Invalid Page Size Range")
            self.skip = (self.p - 1) * self.p_size
            self.limit = self.p_size
