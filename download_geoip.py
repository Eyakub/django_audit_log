import os
import requests
import tarfile
import shutil
from pathlib import Path

def download_geoip():
    # Create geoip directory if it doesn't exist
    geoip_dir = Path('geoip')
    geoip_dir.mkdir(exist_ok=True)

    print("Please download the GeoLite2 databases from MaxMind:")
    print("1. Sign up for a free account at https://www.maxmind.com/en/geolite2/signup")
    print("2. Go to https://www.maxmind.com/en/accounts/current/geoip/downloads")
    print("3. Download 'GeoLite2-Country.tar.gz' and 'GeoLite2-City.tar.gz'")
    print("4. Place them in the 'geoip' directory")
    print("\nAfter downloading, run this script again to extract the files.")

    country_tar = geoip_dir / 'GeoLite2-Country.tar.gz'
    city_tar = geoip_dir / 'GeoLite2-City.tar.gz'

    if country_tar.exists() and city_tar.exists():
        print("\nExtracting files...")

        with tarfile.open(country_tar, 'r:gz') as tar:
            for member in tar.getmembers():
                if member.name.endswith('.mmdb'):
                    tar.extract(member, path=geoip_dir)
                    shutil.move(
                        geoip_dir / member.name,
                        geoip_dir / 'GeoLite2-Country.mmdb'
                    )
                    break

        with tarfile.open(city_tar, 'r:gz') as tar:
            for member in tar.getmembers():
                if member.name.endswith('.mmdb'):
                    tar.extract(member, path=geoip_dir)
                    shutil.move(
                        geoip_dir / member.name,
                        geoip_dir / 'GeoLite2-City.mmdb'
                    )
                    break

        country_tar.unlink()
        city_tar.unlink()

        print("GeoIP databases have been extracted successfully!")
    else:
        print("\nPlease download the required files first.")


if __name__ == '__main__':
    download_geoip()
