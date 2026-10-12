variable "bucket" {
  description = "Name of the S3 bucket to create"
  type        = string
}

variable "aws_default_region" {
  description = "AWS region where resources will be created"
  type        = string
  default     = "us-east-1"
}

variable "enable_lifecycle" {
  description = "Whether to enable lifecycle rules for the S3 bucket"
  type        = bool
  default     = false
}

variable "expire_days" {
  description = "Number of days after which objects should expire"
  type        = number
  default     = null
}

variable "noncurrent_version_expiration" {
  description = "Number of days after which non-current object versions should expire"
  type        = number
  default     = null
}

variable "acl" {
  description = "ACL for the S3 bucket"
  type        = string
  default     = "private"
}

variable "versioning" {
  description = "Whether to enable versioning for the S3 bucket"
  type        = bool
  default     = false
}

variable "force_destroy" {
  description = "Whether to force destroy the bucket even if it contains objects"
  type        = bool
  default     = false
}

variable "cloud_tags" {
  description = "Additional tags to apply to resources"
  type        = map(string)
  default     = {}
}
