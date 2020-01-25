医学命名实体识别demo：
       
      数据集：github.com/yixiu00001/LSTM-CRF-medical/tree/master/data_path
      实体：疾病名称/DISEASE、症状/SYMPTOM、身体部位/BODY
      模型：word2vector+bilstm+crf
      结果(130轮)测试集：精准率89.97%  召回率90.51%  F1调和90.24
                         crf loss: 2.695572
     模型：bert+bilstm+crf
     训练：bert与bilstm添加全连接，embedding:768-->120
           固定bert层，迁移上一个模型的bilstm层+全连接层参数初始化
     结果(2轮)测试集：精准率53.63%  召回率50.06%  F1调和51.78                                           crf loss: 22.974451

生物化学关系抽取demo：

     数据集：非NA数据集 11k (github.com/qq547276542/Agriculture_KnowledgeGraph/)
             NA数据集 12k (维基百科匹配)
     关系类别：NA，instance of，subclass of，parent taxon
     模型：pcnn+BagAttention
     结果(35轮)测试集：非NA准确率(精准率)0.8366  total准确率0.9553 auc: 0.8987
                       前15轮 GradientDescentOptimizer(0.5)不稳定 auc: 0.8293
                       后20轮迁移参数使用AdamOptimizer(0.001)
问诊问答demo:

     数据集：https://github.com/zhangsheng93/cMedQA2
     模型：seq2seq、transformer、transformer-xl、seqgan
