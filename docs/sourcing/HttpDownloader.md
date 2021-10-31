# HttpDownloader

`HttpDownloader` class is used for retrieving files from remote sources.

## Retrieving image files from HTTP sources.

The sample below:

- Utilizes `DownloadKeyPair` class to build a list of download targets.
- It then constructs an `HttpDownloader` class by providing the download targets
- It then triggers the download operations using the `execute` method.

```py
from ipynta.sourcing import DownloadKeyPair
from ipynta.sourcing import HttpDownloader

ICON_PATH_URL = "https://logos-download.com/wp-content/uploads/2016/10/"
OUT_PATH = "./imgs/icons/python/"

download_list = [
  DownloadKeyPair(f"{ICON_PATH_URL}Python_logo_icon.png", f"{OUT_PATH}icon.png"),
  DownloadKeyPair(f"{ICON_PATH_URL}Python_logo_wordmark.png", f"{OUT_PATH}banner.png"),
]

downloader = HttpDownloader(download_list)
downloader.execute()
```

## Retrieving image datasets from HTTP sources

The sample below:

- Utilizes `DownloadKeyPair` class to describe an open-source dataset download from an HTTP source.
- It then constructs an `HttpDownloader` class by providing the a download list.
- It then triggers the download operations using the `execute` method.
- You can utilize `TarExtractor` class to extract the images to a local directory.

```py
from ipynta.sourcing import DownloadKeyPair
from ipynta.sourcing import HttpDownloader
from ipynta.extractors import TarExtractor

TAR_FILE = "./raw/pets.tar.gz"
DATA_PATH = "/train/pets"

download_list = [
  DownloadKeyPair("https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz", TAR_FILE)
]

downloader = HttpDownloader(download_list)
downloader.execute()

extractor = TarExtractor(TAR_FILE, DATA_PATH)
extractor.execute()
```