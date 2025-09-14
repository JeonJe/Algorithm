class Solution {
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
        int totalPeople = languages.length;

        //사람마다 배운 언어 집합
        Set<Integer>[] langByPerson = new Set[totalPeople + 1];
        for(int personId = 1; personId <= totalPeople; personId++) {
            langByPerson[personId] = new HashSet<>();
            for(int lang : languages[personId - 1]) {
                langByPerson[personId].add(lang);
            }
        }

        //대화가 불가능한 관계 확인 -> 교육 대상
        Set<Integer> needTeaching = new HashSet<>();
        for(int[] friendship : friendships) {
            int personA = friendship[0];
            int personB = friendship[1];

            boolean canCommunicate = false;
            for(int lang : langByPerson[personA]) {
                if(langByPerson[personB].contains(lang)) {
                    canCommunicate = true;
                    break;
                }
            }

            if(!canCommunicate) {
                needTeaching.add(personA);
                needTeaching.add(personB);
            }
        }

        if(needTeaching.isEmpty()) {
            return 0;
        }

        // 후보자들 중에서 각 언어를 아는 사람 수 카운트
        int[] knownCountByLanguage = new int [n + 1];
        for(int personId : needTeaching) {
            for(int lang : langByPerson[personId]) {
                knownCountByLanguage[lang]++;
            }
        }

        // 후보자들 중에서 각 언어를 아는 사람 수 카운트
        int maxAlreadyKnow = 0;
        for(int lang = 1; lang <= n; lang++) {
            maxAlreadyKnow = Math.max(maxAlreadyKnow, knownCountByLanguage[lang]);
        }

        //전체 후보 수 - 사람들이 가장 많이 알고 있는 언어를 알고 있는 사람의 수 = 배워야할 사람의 최소 수 
        return needTeaching.size() - maxAlreadyKnow;
    }
}