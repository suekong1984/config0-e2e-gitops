resource "aws_s3_bucket" "default" {
  bucket        = var.bucket
  acl           = var.acl
  force_destroy = var.force_destroy

  tags = merge(
    var.cloud_tags,
    {
      Product = "s3"
    },
  )

  versioning {
    enabled = var.versioning
  }

  # Emit the lifecycle_rule only when lifecycle is enabled, and each action
  # block only when its variable is set. A rule needs at least one action, and a
  # nested block whose day count is null (the default) makes the AWS provider
  # perpetually re-plan an empty block, so both are gated instead of always
  # declared.
  dynamic "lifecycle_rule" {
    for_each = var.enable_lifecycle ? [1] : []

    content {
      enabled = true

      dynamic "expiration" {
        for_each = var.expire_days == null ? [] : [var.expire_days]

        content {
          days = expiration.value
        }
      }

      dynamic "noncurrent_version_expiration" {
        for_each = var.noncurrent_version_expiration == null ? [] : [var.noncurrent_version_expiration]

        content {
          days = noncurrent_version_expiration.value
        }
      }
    }
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}
