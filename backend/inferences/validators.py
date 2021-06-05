from django.core.exceptions import ValidationError

ACCEPTABLE_FILE_SIZE_LIMIT = 10485760  # 10MB


def validate_file_size(file):
    limit = ACCEPTABLE_FILE_SIZE_LIMIT
    if file.size > limit:
        raise ValidationError('File too large. Size should not exceed 10 MB.')
