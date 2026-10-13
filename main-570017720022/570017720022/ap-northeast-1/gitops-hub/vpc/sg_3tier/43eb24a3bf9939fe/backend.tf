terraform {
  backend "s3" {
    bucket = "config0-stateful-62635338"
    key    = "targets/570017720022/ap-northeast-1/gitops-hub/vpc/sg_3tier/43eb24a3bf9939fe/terraform.tfstate"
    region = "ap-northeast-1"
  }
}
