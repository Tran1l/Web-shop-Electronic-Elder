from django.shortcuts import render
from products.models import ProductCatagory, Product
import boto3.s3 as bs3
import boto3
from .models import ProductCatagory
from electronic_elder.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from botocore.client import Config
import base64
from io import BytesIO


# Create your views here.
def catalog(request):
    context = {
        "category": ProductCatagory.objects.all(),
    }
    return render(request, "products/catalog.html")


def catalog_thinkpad(request):
    # connection to minio database
    s3 = boto3.resource(
        "s3",
        endpoint_url="http://s3:9000",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        config=Config(signature_version="s3v4"),
        region_name="eu-west-1",
    )

    buf = BytesIO()
    s3.Bucket("media-bucket").download_fileobj("thinkpad.png", buf)
    # cleaned_img = base64.b64encode(buf.getvalue()).decode('utf-8')
    # class for context

    context = {"bytes": base64.b64encode(buf.getvalue()).decode("utf-8")}
    return render(request, "products/catalog_thinkpad.html", context=context)


def index(request):
    context = {
        "title": "Electronic Elder",
    }
    return render(request, "products/index.html", context=context)


def contacts(request):
    return render(request, "products/contacts.html")


def how_buy(request):
    return render(request, "products/how_buy.html")


def company(request):
    return render(request, "products/company.html")
