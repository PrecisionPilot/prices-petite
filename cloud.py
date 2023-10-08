from google.oauth2.service_account import Credentials

# Specify the path to the service account key file
key_path = 'Auth/Google Cloud.json'

# Create a credentials object
creds = Credentials.from_service_account_file(key_path)

def detect_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision

    client = vision.ImageAnnotatorClient(credentials=creds)

    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations

    # print(f"Number of objects found: {len(objects)}")
    # for object_ in objects:
    #     print(f"\n{object_.name} (confidence: {object_.score})")
    #     print("Normalized bounding polygon vertices: ")
    #     for vertex in object_.bounding_poly.normalized_vertices:
    #         print(f" - ({vertex.x}, {vertex.y})")

    print(objects[0].name)

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient(credentials=creds)

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")

    for text in texts:
        print(f'\n"{text.description}"')

        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]

        print("bounds: {}".format(",".join(vertices)))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )