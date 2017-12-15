import mediacloud, datetime
import logging, unittest

from config import MY_API_KEY


class mediacloudTest(unittest.TestCase):
    def setUp(self):
        self.mc = mediacloud.api.MediaCloud(MY_API_KEY)

        # create logger
        logger = logging.getLogger('testlogger')
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        # file handler
        fh = logging.FileHandler(r'/log.txt')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        # 'application' code
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')

    def connectMC(self):


        #API KEY CHECK

        assert self.MY_API_KEY is not None


        assert mc is not None
        print("connecting API")
        logging.debug("Error connecting API")

    def testCount(self):
        mc = mediacloud.api.MediaCloud(MY_API_KEY)



        res = mc.sentenceCount("trump", solr_filter=[
            mc.publish_date_query(datetime.date(2016, 9, 1), datetime.date(2016, 9, 31)), 'tags_id_media:1'])
        count = res['count']

        ## count1 = res['count']
        print("sentences: ", count)
        assert count > 0
        logging.error("Error counting sentences")






if __name__ == "__main__":
    unittest.main()