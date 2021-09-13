terraform {
    backend "s3" {
        bucket = "sw-k8s-backend"
        key = "terraform.tfstate"
        region = "us-east-1"
    }
}