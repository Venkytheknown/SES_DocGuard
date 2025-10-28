def train_model(model, train_data, val_data, config):
    from transformers import Trainer, TrainingArguments

    training_args = TrainingArguments(
        output_dir=config['output_dir'],
        evaluation_strategy="epoch",
        learning_rate=config['learning_rate'],
        per_device_train_batch_size=config['train_batch_size'],
        per_device_eval_batch_size=config['eval_batch_size'],
        num_train_epochs=config['num_epochs'],
        weight_decay=config['weight_decay'],
        logging_dir=config['logging_dir'],
        logging_steps=config['logging_steps'],
        save_steps=config['save_steps'],
        load_best_model_at_end=True,
        metric_for_best_model=config['metric_for_best_model'],
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_data,
        eval_dataset=val_data,
        compute_metrics=config['compute_metrics'],
    )

    trainer.train()
    trainer.save_model(config['output_dir'])

def load_model(model_path):
    from transformers import AutoModelForSequenceClassification

    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return model

def main():
    import yaml

    with open('configs/training_config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    train_data = ...  # Load your training data here
    val_data = ...    # Load your validation data here

    model = load_model(config['model_path'])
    train_model(model, train_data, val_data, config)

if __name__ == "__main__":
    main()