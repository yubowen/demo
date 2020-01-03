# demo
医学问诊问答，NER，关系抽取
tensorflow1.9.0 官网的2.0教程8g内存只够处理不到50token,可能是没有释放当前token之前包括encoder,attention的内存
                transformer类模型可以用

1.chatbot：问诊问答
  数据：https://github.com/zhangsheng93/cMedQA2
  根据数据修改了下data_util,处理中文字符，定义dictionary
  
  conv_seq/goodle_nmt/transformer/transfermer-xl源码：
  https://github.com/huseinzol05/NLP-Models-Tensorflow/tree/master/chatbot
  
  seqgan源码：
  https://github.com/zhaoyingjun/TensorFlow-Coding/tree/master/lessonTen/seqGan%20chatbotv2.0
