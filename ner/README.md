医学命名实体识别demo：
       
      数据集：github.com/yixiu00001/LSTM-CRF-medical/tree/master/data_path
      实体：疾病名称/DISEASE、症状/SYMPTOM、身体部位/BODY
      模型：word2vector+bilstm+crf
      结果(130轮)测试集：精准率89.97%  召回率90.51%  F1调和90.24
                         crf loss: 2.695572
      模型：bert+bilstm+crf
      训练：bert与bilstm添加全连接，embedding:768-->120
           固定bert层，迁移上一个模型的bilstm层+全连接层参数初始化
      结果(2轮)测试集：精准率53.63%  召回率50.06%  F1调和51.78                                           
                     crf loss: 22.974451
      
      albert+bilstm+crf  fintune
      tiny版训练80+轮后效果与基本bilstm+crf还相差一点1%不到
      base版本第九轮已超过基本bilstm+crf 12轮结果：
            accuracy:  98.96%; precision:  91.79%; recall:  90.71%; FB1:  91.25
