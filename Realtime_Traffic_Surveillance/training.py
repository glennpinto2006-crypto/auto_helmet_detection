from ultralytics import YOLO
from multiprocessing import freeze_support

def main():
    # Load model
    model = YOLO("yolo26s.pt")

    # Train
    model.train(
        data=r"....\vehdata\data.yaml",
        epochs=150,
        imgsz=640,
        batch=16,
        device=0,
    )

if __name__ == "__main__":
    freeze_support()
    main()