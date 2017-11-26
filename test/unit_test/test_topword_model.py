import numpy as np
import pandas as pd
from lexos.helpers.error_messages import SEG_NON_POSITIVE_MESSAGE, \
    EMPTY_NP_ARRAY_MESSAGE, EMPTY_LIST_MESSAGE
from lexos.models.topword_model import TopwordModel, TopwordTestOptions
from lexos.receivers.topword_receiver import TopwordFrontEndOption


# ---------------------------- Test for z-test ------------------------------
class TestZTest:
    def test_normal_case(self):
        assert round(TopwordModel._z_test(p1=0.1, pt=0.3, n1=10, nt=1000), 2) \
            == -1.38
        assert round(TopwordModel._z_test(p1=0.3, pt=0.1, n1=100, nt=100), 2) \
            == 3.54
        assert TopwordModel._z_test(p1=1, pt=1, n1=100, nt=100) == 0

    def test_special_case(self):
        try:
            _ = TopwordModel._z_test(p1=0.1, pt=0.3, n1=100, nt=0)
            raise AssertionError("Error message did not raise")
        except AssertionError as error:
            assert str(error) == SEG_NON_POSITIVE_MESSAGE

        try:
            _ = TopwordModel._z_test(p1=0.1, pt=0.3, n1=0, nt=100)
            raise AssertionError("Error message did not raise")
        except AssertionError as error:
            assert str(error) == SEG_NON_POSITIVE_MESSAGE
# ---------------------------------------------------------------------------


# -------------------- Test method analyze all to para ----------------------
# Create test suits for normal cases
test_dtm = pd.DataFrame(data=np.array([(1, 1, 0, 0), (0, 0, 1, 10)]),
                            index=np.array([0, 1]),
                            columns=np.array(["A", "B", "C", "D"]))
test_id_temp_label_map = {0: "F1", 1: "F2"}
