import omegaconf
from openhands.apis.classification_model import ClassificationModel
from openhands.core.exp_utils import get_trainer
import warnings

warnings.filterwarnings("ignore", category=UserWarning) 

if __name__ == "__main__":
    cfg = omegaconf.OmegaConf.load("./wlasl_bert/wlasl/bert/config.yaml")
    trainer = get_trainer(cfg)
    model = ClassificationModel(cfg=cfg, trainer=trainer)
    model.init_from_checkpoint_if_available()
    model.fit() 