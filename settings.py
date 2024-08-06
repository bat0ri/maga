from dotenv import load_dotenv
import os

load_dotenv()


class Direction:

    def __init__(self, url: str, places: int, name: str):
        self.url = url
        self.places = places
        self.name = name
        self.df = None
        self.admitted = None

    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, value):
        self._df = value

    @property
    def admitted(self):
        return self._admitted

    @admitted.setter
    def admitted(self, value):
        self._admitted = value

    @property
    def places(self):
        return self._places

    @places.setter
    def places(self, value):
        if not isinstance(value, int):
            raise TypeError("places must be an integer")
        self._places = value


class Tables:
    def __init__(self):
        self.IST = Direction(url=os.getenv("URL_IST"), places=39, name="IST")
        self.FIIT = Direction(url=os.getenv("URL_FIIT"), places=20, name="FIIT")
        self.IB = Direction(url=os.getenv("URL_IB"), places=10, name="IB")
        self.PM = Direction(url=os.getenv("URL_PM"), places=15, name="PM")
        self.PMI = Direction(url=os.getenv("URL_PMI"), places=28, name="PMI")
        self.BI = Direction(url=os.getenv("URL_BI"), places=10, name="BI")
        self.PI = Direction(url=os.getenv("URL_PI"), places=14, name="PI")

    def get_directions(self):
        return [self.IST, self.FIIT, self.IB, self.PM, self.PMI, self.BI, self.PI]
    
    def get_dfs(self):
        return [self.IST.df, self.FIIT.df, self.IB.df, self.PM.df, self.PMI.df, self.BI.df, self.PI.df]


config = Tables()
