#!/bin/bash

# Done on the fly during interview:
#
# Provide a list of IAM users with active keys over 60 days old

for u in $(aws iam list-users --query='Users[].UserName' --output text)
do
    aws iam list-access-keys --user $u --query='AccessKeyMetadata[].[UserName,Status,CreateDate]' --output text | \
    gawk 'BEGIN { expiretime=systime() - (60 * 86400) }
        $2 == "Active" {
            gsub(/[-,:,T,Z]/, " ", $3);
            createtime = mktime($3);
            if (createtime < expiretime) {
                printf("%s keys over 60 days old\n", $1)
            }
        }'
done

