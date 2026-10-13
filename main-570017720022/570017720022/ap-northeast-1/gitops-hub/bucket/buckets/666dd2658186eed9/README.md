# S3 Bucket Module

This OpenTofu module creates an AWS S3 bucket with configurable settings for versioning, lifecycle rules, and server-side encryption.

## Features

- Creates a single S3 bucket with configurable settings
- Supports bucket versioning
- Configurable lifecycle rules for object expiration
- Default server-side encryption with AES256
- Customizable ACL settings
- Optional force destroy capability

## Usage

```hcl
module "s3_bucket" {
  source = "./path/to/module"
  
  bucket             = "my-example-bucket"
  aws_default_region = "us-east-1"
  versioning         = true
  
  # Optional lifecycle configuration
  enable_lifecycle            = true
  expire_days                 = 90
  noncurrent_version_expiration = 30
  
  # Additional tags
  cloud_tags = {
    Environment = "Production"
    Team        = "DevOps"
  }
}
```

## Variables

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| bucket | Name of the S3 bucket to create | string | n/a | yes |
| aws_default_region | AWS region where resources will be created | string | "us-east-1" | no |
| enable_lifecycle | Whether to enable lifecycle rules for the S3 bucket | bool | false | no |
| expire_days | Number of days after which objects should expire | number | null | no |
| noncurrent_version_expiration | Number of days after which non-current object versions should expire | number | null | no |
| acl | ACL for the S3 bucket | string | "private" | no |
| versioning | Whether to enable versioning for the S3 bucket | bool | null | no |
| force_destroy | Whether to force destroy the bucket even if it contains objects | bool | null | no |
| cloud_tags | Additional tags to apply to resources | map(string) | {} | no |

## Outputs

| Name | Description |
|------|-------------|
| arn | ARN of the created S3 bucket |

## Notes

- Default server-side encryption is enabled with AES256 algorithm
- Be careful when setting `force_destroy = true` as it will delete all objects in the bucket when the bucket is destroyed

## License

Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.