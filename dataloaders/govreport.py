import os
from dataloaders.unified_data import ReportSumBase
from config import Config
import torch

config = Config()

MAP = {'train': 'train', 'valid': 'val', 'test': 'test'}

class GovReport(ReportSumBase):
    """The GovReport dataset."""

    def __init__(self, mode, retriever_tokenizer, generator_tokenizer):
        super(GovReport, self).__init__(mode, retriever_tokenizer, generator_tokenizer)

        self.root = os.path.join('data', 'GovReport')

        self.cached_features_file = os.path.join(self.root, '{}_cached_govreport'.format(MAP[self.mode]))

        self.file_name = os.path.join(self.root, 'govreport_{}_with_oracle.jsonl'.format(MAP[self.mode]))
        self.load_features_from_cache()

    def get_features(self):
        self.features = self.read_report_summarization()
        print('GovReport data successfully read.')
    
    def print_filtered_samples(self, session):
        report = session["report"]
        summary = session["summary"]
        if len(report) < 10:
            print("----------- 被滤掉的报告内容 -----------")
            print("Report content is too short:")
            print(report[:8])
            print("----------- 被滤掉的摘要内容 -----------")
            print("Summary content is too short:")
            print(summary[:300])
            print("----------- 结束 -----------")

