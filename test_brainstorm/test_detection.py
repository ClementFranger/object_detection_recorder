import PIL
import numpy

from brainstorm.detection import Detection
from workout.model.trained_model import TrainedModel
from test_brainstorm import Test
from workout.image import PathImage
from workout.labelimg.data import Data


class TestDetection(Test):
    image = r'C:\Users\Minifranger\Documents\python_scripts\workout\test_workout\test_vision\img.png'

    def setUp(self):
        super().setUp()
        self.data = Data.factory(source=self.data)
        self.trained_model = TrainedModel.factory(source=self.graph)
        self.detections = Detection.factory()

    def test_detect(self):
        Detection.instance.detect(model=TrainedModel.instance.model_with_signatures, image=PathImage(path=self.image))
        assert isinstance(Detection.instance.detections, dict)
        assert isinstance(Detection.instance.num_detections, int)
        assert isinstance(Detection.instance.detection_classes, numpy.ndarray)
        assert all([isinstance(c, numpy.int64) for c in Detection.instance.detection_classes])
        assert isinstance(Detection.instance.detection_scores, numpy.ndarray)
        assert all([isinstance(s, numpy.float32) for s in Detection.instance.detection_scores])

    def test_draw_boxes(self):
        Detection.instance.detect(model=TrainedModel.instance.model_with_signatures,
                                  image=PathImage(path=self.dofus_image))
        image = Detection.instance.draw_boxes(category_index=Data.instance.category_index)

        im = PIL.Image.fromarray(image)
        im.save("test_draw_boxes.jpg")
