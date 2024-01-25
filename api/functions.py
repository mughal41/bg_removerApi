from PIL import Image
from rembg import new_session, remove
from io import BytesIO
import uuid
import os
from pytz import country_timezones

# input_path = 'media/data/input.png'


def remove_bg(file):
    try:
        if not os.path.exists('media/data'):
            os.makedirs('media/data')
        file_extension = os.path.splitext(file.name)[1]

        # Remove the leading dot (.) from the extension
        file_extension = file_extension.lstrip(".")
        image_data = file.read()
        output_path = f'media/data/{uuid.uuid4()}.png'#{file_extension}
        image_stream = BytesIO(image_data)
        input = Image.open(image_stream)
        model_name = "u2net_human_seg"
        session = new_session(model_name)
        # output = remove(input, session=session)
        output = remove(
            input,
            alpha_matting=True,
            alpha_matting_foreground_threshold=270,
            alpha_matting_background_threshold=20,
            alpha_matting_erode_size=11,
            # bgcolor=(255, 255, 255, 255),
            session=session
        )

        output.save(output_path)
        return output_path.split("media/")[1]
    except OSError as oe:
        print(f"{oe}")
        output = output.convert("RGB")
        output.save(output_path)
        return output_path.split("media/")[1]


def get_country_code(time_zone):
    try:
        print(time_zone)
        time_zone = f"{time_zone.split('/')[0].capitalize()}/{time_zone.split('/')[1].capitalize()}"
        timezone_country = {}
        for countrycode in country_timezones:
            timezones = country_timezones[countrycode]
            for timezone in timezones:
                timezone_country[timezone] = countrycode
        return {'status': True, 'data': {'id': timezone_country[time_zone]}}
    except KeyError:
        return {'status': False, 'data': {'message': f'country for {time_zone} not found'}}
    except AttributeError:
        return {'status': False, 'data': {'message': f'invalid param sent'}}