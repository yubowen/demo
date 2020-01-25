生物化学关系抽取demo：

     数据集：非NA数据集 11k (github.com/qq547276542/Agriculture_KnowledgeGraph/)
             NA数据集 12k (维基百科匹配)
     关系类别：NA，instance of，subclass of，parent taxon
     模型：pcnn+BagAttention
     结果(35轮)测试集：非NA准确率(精准率)0.8366  total准确率0.9553 auc: 0.8987
                       前15轮 GradientDescentOptimizer(0.5)不稳定 auc: 0.8293
                       后20轮迁移参数使用AdamOptimizer(0.001)
