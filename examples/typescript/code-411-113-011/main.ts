
import { Camera, CameraResultType } from '@capacitor/camera';
import { Geolocation } from '@capacitor/geolocation';
import { Filesystem, Directory } from '@capacitor/filesystem';

async function capturePhoto() {
    const photo = await Camera.getPhoto({
        quality: 90,
        allowEditing: false,
        resultType: CameraResultType.Uri
    });

    const coordinates = await Geolocation.getCurrentPosition();

    const fileName = `photo_${Date.now()}.jpg`;
    await Filesystem.writeFile({
        path: fileName,
        data: photo.base64String,
        directory: Directory.Documents
    });

    return {
        photo: photo.webPath,
        location: {
            latitude: coordinates.coords.latitude,
            longitude: coordinates.coords.longitude
        }
    };
}
