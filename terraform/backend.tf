terraform {
    backend "s3" {
        bucket = "sw-k8s"
        key = "terraform.tfstate"
        region = "us-east-1"
    }
}