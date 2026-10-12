terraform {
  backend "s3" {
    bucket = "config0-stateful-62635338"
    key    = "targets/570017720022/ap-northeast-1/gitops-hub/vpc/vpc_simple/03dd8318ef1719a9/terraform.tfstate"
    region = "ap-northeast-1"
  }
}
