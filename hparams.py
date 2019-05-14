from collections import defaultdict

BASE_HPARAMS = defaultdict(
  description='base',
  friends_train='./data/friends_train_dialogs',
  friends_test='./data/friends_test_dialogs',
  
  save_dir='/mnt/raid5/yks/EmotionX/saves',
  log_dir='/mnt/raid5/yks/EmotionX/logs',
  model_name='',
  wce_log='train_loss',
  uwa_log='test_UWA',
  wa_log='test_WA',
  micro_f1_log='micro_f1',

  bert_type = 'bert-base-cased',
  cls_token='[CLS]',
  sep_token='[SEP]',
  pad_token='[PAD]',
  sep_id=102,
  pad_id=0,

  hidden_size=768,
  n_class=4+1, # neutral, joy, sadness, anger + OOD

  n_epoch=50,
  batch_size=4,
  print_per=200,
  learning_rate=5e-5,
  dropout=0.2,
  clip=5,

  cls_emb=False,
  seg_emb=False,
)

YKSMODEL_BERT_FC1_HPARAMS = BASE_HPARAMS.copy()
YKSMODEL_BERT_FC1_HPARAMS.update(
  #model_name='bert_fc1',
  #model_name='bert_fc2_selu',
  #model_name='shf_slr_bert_fc2_selu',
  #model_name='shf_5e5slr_bert_fc2_selu_w1._gradclip',
  #model_name='bert_selu_gradclip_seg',
  model_name='bert_selu_gradclip',
)