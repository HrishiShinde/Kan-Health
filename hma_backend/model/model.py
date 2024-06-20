import os
import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Trainer, TrainingArguments, DataCollatorForSeq2Seq

class HealthAI:
    def __init__(self):
        self.model_path = os.getenv("MODEL_PATH")
        self.model = None
        self.tokenizer = None
        self.load_model()
        self.model.eval()

    def fine_tune(self):
        dataset = load_dataset("omi-health/medical-dialogue-to-soap-summary")

        # Load tokenizer and model
        model_name = "t5-small"  # Use a sequence-to-sequence model like T5
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

        tokenized_datasets = dataset.map(self.tokenize_function, batched=True)

        # Define training arguments
        training_args = TrainingArguments(
            output_dir="./results",
            evaluation_strategy="epoch",
            per_device_train_batch_size=8,
            per_device_eval_batch_size=8,
            num_train_epochs=3,
            logging_dir='./logs',
        )

        # Initialize data collator for dynamic padding
        data_collator = DataCollatorForSeq2Seq(self.tokenizer, model=self.model)

        # Initialize Trainer
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=tokenized_datasets["train"],
            eval_dataset=tokenized_datasets["test"],
            data_collator=data_collator
        )

        # Fine-tune the model
        trainer.train()

        # Save the fine-tuned model
        self.model.save_pretrained(self.model_path)
        self.tokenizer.save_pretrained(self.model_path)

    def tokenize_function(self, examples):
        inputs = self.tokenizer(examples["dialogue"], padding="max_length", truncation=True, max_length=512)
        targets = self.tokenizer(examples["soap"], padding="max_length", truncation=True, max_length=512)
        inputs["labels"] = targets["input_ids"]
        return inputs

    def load_model(self):
        if not os.path.exists(self.model_path):
            self.fine_tune()

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_path)

    def generate_health_plan(self, query):
        # Tokenize the input data
        inputs = self.tokenizer(query, return_tensors="pt", truncation=True, padding="max_length", max_length=512)

        # Generate output using the model
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=inputs['input_ids'],
                attention_mask=inputs['attention_mask'],
                max_length=512,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                num_beams=5
            )

        # Decode the generated output
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def generate_health_plan2(self, query):
        # Tokenize the input data
        inputs = self.tokenizer(query, return_tensors="pt", truncation=True, padding="max_length", max_length=512)

        # Generate output using the model
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=inputs['input_ids'],
                attention_mask=inputs['attention_mask'],
                max_length=512,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                num_beams=5
            )

        # Decode the generated output
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Return the generated text as JSON response
        return {'generated_health_plan': generated_text}
