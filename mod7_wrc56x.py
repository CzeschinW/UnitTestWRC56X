import unittest
import re
from FrontEnd import FrontEnd

class frontEndTest(unittest.TestCase):

    def setUp(self): 
        self.setup = FrontEnd.frontEnd
       
    def tearDown(self):
        self.ticker = ""
        self.chartType = 0
        self.timeSeries = 0
        self.startDate = {"year": 0, "month": 0, "day": 0}
        self.endDate = {"year": 0, "month": 0, "day": 0}
        print("Teardown called . . .")
        

    def test_func_1(self):
        print("Test 1 called . . .")
        #act 
        tickerTest = self.setup.ticker.isalpha()
        #assert
        self.assertEqual(tickerTest, True)

    def test_func_2(self):
        print("Test 2 called . . .")
        #act 
        chartTypeTest = self.setup.chartType
        if chartTypeTest in range(1, 2):
            check = True
        else:
            check = False
        #assert
        self.assertEqual(check, True)

    def test_func_3(self):
        print("Test 3 called . . .")
        #act 
        timeSeriesTest = self.setup.timeSeries
       
        if timeSeriesTest in range(1, 4):
            check = True
        else:
            check = False
        #assert
        self.assertEqual(check, True)

    def test_func_4(self):
        print("Test 4 called . . .")
        #act 
        intervalTest = self.setup.interval

        if intervalTest in range(1, 5):
            check = True
        else:
            check = False
        #assert
        self.assertEqual(check, True)

    def test_func_5(self):
        print("Test 5 called . . .")
        #act 
        startDateDict = self.setup.startDate
        year = startDateDict.get("year")
        month = startDateDict.get("month")
        day = startDateDict.get("day")

        startDateTest = f"{year}-{month}-{day}"
        print(startDateTest)
        form = re.compile('....-..-..')
        check = form.match(startDateTest) is not None
        #assert
        self.assertEqual(check, True)

    def test_func_6(self):
        print("Test 6 called . . .")
        #act 
        endDateDict = self.setup.endDate
        year = endDateDict.get("year")
        month = endDateDict.get("month")
        day = endDateDict.get("day")

        endDateTest = f"{year}-{month}-{day}"
        print(endDateTest)
        form = re.compile('....-..-..')
        check = form.match(endDateTest) is not None
        #assert
        self.assertEqual(check, True)

if __name__ == "__main__":
    unittest.main()
