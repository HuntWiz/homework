from tests_12_3 import RunnerTest
import logging
import exm_for_tests

class RunnerTest():
    is_frozen = False


    def test_walk(self):
        try:
            runner = exm_for_tests.Runner('Jim', -10)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                runner.walk()
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)



    def test_run(self):
        try:
            runner = exm_for_tests.Runner('Jim', -10)
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                runner.run()
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True )


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        filename='runner_test.log',
                        encoding='utf-8',
                        format='%(levelname)s || %(message)s')

    runner = RunnerTest()
    runner.test_run()
    runner.test_walk()