import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 100 },
    { duration: '5m', target: 100 },
    { duration: '2m', target: 200 },
    { duration: '5m', target: 200 },
    { duration: '2m', target: 300 },
    { duration: '5m', target: 300 },
    { duration: '2m', target: 400 },
    { duration: '5m', target: 400 },
    { duration: '10m', target: 0 },
  ],
};

export default function () {
  const BASE_URL = 'http://pretest-qa.dcidev.id';

  const responses = http.batch([
    ['POST', `${BASE_URL}/api/v1/register/otp/match`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/api/v1/profile/me`, null, { tags: { name: 'PublicCrocs' } }],
    ['POST', `${BASE_URL}/api/v1/profile`, null, { tags: { name: 'PublicCrocs' } }],
    ['POST', `${BASE_URL}/api/v1/profile/education`, null, { tags: { name: 'PublicCrocs' } }],
    ['POST', `${BASE_URL}/api/v1/profile/career`, null, { tags: { name: 'PublicCrocs' } }],
    ['POST', `${BASE_URL}/api/v1/message/send`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/api/v1/message/{user_id}`, null, { tags: { name: 'PublicCrocs' } }],
    ['POST', `${BASE_URL}/api/v1/oauth/sign_in`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/api/v1/oauth/credentials`, null, { tags: { name: 'PublicCrocs' } }],
    ['POST', `${BASE_URL}/api/v1/uploads/cover`, null, { tags: { name: 'PublicCrocs' } }],
    ['POST', `${BASE_URL}/api/v1/uploads/profile/default`, null, { tags: { name: 'PublicCrocs' } }],
    ['DELETE', `${BASE_URL}/api/v1/uploads/profile`, null, { tags: { name: 'PublicCrocs' } }],
    ['POST', `${BASE_URL}/api/v1/uploads/profile`, null, { tags: { name: 'PublicCrocs' } }],
  ]);

  sleep(1);
}