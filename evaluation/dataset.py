evaluation_dataset = [

    # =====================================================
    # Employee Handbook
    # =====================================================

    {
        "question": "Where is the HR department located?",
        "ground_truth": "The HR department is located on the third floor."
    },

    {
        "question": "What are the office timings?",
        "ground_truth": "Office timings are from 9:00 AM to 6:00 PM."
    },

    {
        "question": "How many casual leaves do employees receive every year?",
        "ground_truth": "Employees receive 20 casual leaves every year."
    },

    {
        "question": "Can employees work from home?",
        "ground_truth": "Employees can work from home two days a week with manager approval."
    },

    {
        "question": "How many days can employees work from home?",
        "ground_truth": "Employees can work from home two days a week with manager approval."
    },

    {
        "question": "When should leave requests be submitted?",
        "ground_truth": "Employees should submit leave requests at least two days in advance."
    },

    {
        "question": "How often are performance reviews conducted?",
        "ground_truth": "Performance reviews are conducted twice a year."
    },

    {
        "question": "Where should employees submit expense reimbursement requests?",
        "ground_truth": "Expense reimbursement requests should be submitted through the HR portal."
    },

    {
        "question": "Who should employees contact regarding payroll issues?",
        "ground_truth": "Employees should contact the HR department regarding payroll issues."
    },

    {
        "question": "What dress code should employees follow?",
        "ground_truth": "Employees should follow the company's business casual dress code."
    },

    # =====================================================
    # Attention Is All You Need
    # =====================================================

    {
        "question": "Who proposed the Transformer architecture?",
        "ground_truth": "The Transformer architecture was proposed by Ashish Vaswani and seven co-authors in the paper 'Attention Is All You Need'."
    },

    {
        "question": "What architecture does the paper introduce?",
        "ground_truth": "The paper introduces the Transformer, a sequence transduction model based entirely on attention mechanisms."
    },

    {
        "question": "What does the Transformer replace?",
        "ground_truth": "The Transformer replaces recurrence and convolutions with attention mechanisms."
    },

    {
        "question": "Why is the Transformer faster to train than recurrent models?",
        "ground_truth": "Because it removes sequential recurrence, allowing significantly greater parallelization during training."
    },

    {
        "question": "What is self-attention?",
        "ground_truth": "Self-attention is an attention mechanism that relates different positions within the same sequence to compute a representation of that sequence."
    },

    {
        "question": "What attention mechanism is introduced in the paper?",
        "ground_truth": "The paper introduces Scaled Dot-Product Attention."
    },

    {
        "question": "Why is the dot product scaled in Scaled Dot-Product Attention?",
        "ground_truth": "The dot products are scaled by the square root of the key dimension to prevent large values that push the softmax into regions with very small gradients."
    },

    {
        "question": "What is Multi-Head Attention?",
        "ground_truth": "Multi-Head Attention projects queries, keys and values into multiple subspaces and performs attention in parallel before concatenating the results."
    },

    {
        "question": "How many encoder layers does the base Transformer use?",
        "ground_truth": "The encoder consists of six identical layers."
    },

    {
        "question": "How many decoder layers does the base Transformer use?",
        "ground_truth": "The decoder consists of six identical layers."
    },

    {
        "question": "What is positional encoding used for?",
        "ground_truth": "Positional encoding provides information about the order of tokens because the Transformer contains neither recurrence nor convolution."
    },

    {
        "question": "What functions are used for positional encoding?",
        "ground_truth": "The positional encoding uses sine and cosine functions of different frequencies."
    },

    {
        "question": "Which optimizer is used to train the Transformer?",
        "ground_truth": "The Transformer is trained using the Adam optimizer."
    },

    {
        "question": "What BLEU score did the Transformer achieve on the WMT 2014 English-to-German translation task?",
        "ground_truth": "The Transformer (big) achieved a BLEU score of 28.4."
    },

    {
        "question": "What is the main conclusion of the paper?",
        "ground_truth": "The paper concludes that attention alone is sufficient for high-quality sequence transduction, enabling faster training and state-of-the-art translation performance."
    }

]