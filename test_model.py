import tensorflow as tf
import numpy as np

def test_model_loading():
    """Test if the model can be loaded and its input shape"""
    try:
        model = tf.keras.models.load_model("models/plant_disease_recog_model_pwp.keras")
        print("✓ Model loaded successfully")
        
        # Check input shape
        input_shape = model.input_shape
        print(f"Model input shape: {input_shape}")
        
        # Test with dummy RGB image
        dummy_input = np.random.random((1, 161, 161, 3))
        prediction = model.predict(dummy_input)
        print(f"✓ Prediction successful: {prediction.shape}")
        
        return True
    except Exception as e:
        print(f"✗ Error loading model: {str(e)}")
        return False

if __name__ == "__main__":
    test_model_loading()
