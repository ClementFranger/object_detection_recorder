from brainstorm.recorder import Recorder
from test_brainstorm import Test
from workout.labelimg.data import Data


class TestRecorder(Test):

    def setUp(self):
        self.data = Data.factory(source=self.data)
        self.recorder = Recorder.factory(title=self.title, source=self.graph)

    def test_stream(self):
        self.recorder.stream()
