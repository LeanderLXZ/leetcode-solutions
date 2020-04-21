#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (47.38%)
# Likes:    6142
# Dislikes: 107
# Total Accepted:    461.4K
# Total Submissions: 973.3K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
#
# Example:
#
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#
#

# @lc code=start
class Solution:

    def trap(self, height: List[int]):
        
    #     v_left = self._flow_in_one_way(height)
    #     v_right = self._flow_in_one_way(height[::-1])[::-1]
    #     v_total = 0
    #     for v_l, v_r in zip(v_left, v_right):
    #         v_total += min(v_l, v_r)
    #     return v_total

    # def _flow_in_one_way(self, height):
    #     pre_h = 0
    #     trapped = False
    #     v_list = []
    #     for h_i in height:
    #         if trapped:
    #             if h_i >= h_record:
    #                 h_record = 0
    #                 v_list.append(0)
    #                 trapped = False
    #             else:
    #                 v_list.append(h_record - h_i)
    #         else:
    #             if h_i < pre_h:
    #                 h_record = pre_h
    #                 trapped = True
    #                 v_list.append(h_record - h_i)
    #             else:
    #                 v_list.append(0)
    #         pre_h = h_i
    #     return v_list


        
    #     if height == []:
    #         return 0
    
    #     left_p = 0
    #     left_water_line = 0
    #     right_p = len(height) - 1
    #     right_water_line = 0
    #     v_total = 0

    #     while left_p != right_p:

    #         left_height = height[left_p]
    #         right_height = height[right_p]

    #         if left_height < right_height:
    #             left_water_line = max(left_height, left_water_line)
    #             v_total += left_water_line - left_height
    #             left_p += 1
    #         else:
    #             right_water_line = max(right_height, right_water_line)
    #             v_total += right_water_line - right_height
    #             right_p -= 1

    #     return v_total

    # def _flow_in_one_way(building_list_):
    #     pre_h = 0
    #     trapped = False
    #     v_list = []
    #     for h_i in building_list_:
    #         if trapped:
    #             if h_i >= h_record:
    #                 h_record = 0
    #                 v_list.append(0)
    #                 trapped = False
    #             else:
    #                 v_list.append(h_record - h_i)
    #         else:
    #             if h_i < pre_h:
    #                 h_record = pre_h
    #                 trapped = True
    #                 v_list.append(h_record - h_i)
    #             else:
    #                 v_list.append(0)
    #         pre_h = h_i
    #     return v_list

    # highest = [0, 0]
    # for i, h_i in enumerate(height):
    #     if h_i > highest[1]:
    #         highest = [i, h_i]

    # v_left = _flow_in_one_way(height[:highest[0]])
    # v_right = v_left + _flow_in_one_way(height[highest[0]:][::-1])[::-1]

    # v_total = sum(v_right)

    # return v_total

        def _flow(building_list_):
            water_line = 0
            volume = 0
            for h_i in building_list_:
                water_line = max(water_line, h_i)
                volume += water_line - h_i
            return volume

        i_max = 0
        for i, h_i in enumerate(height):
            if h_i > height[i_max]:
                i_max = i

        return _flow(height[:i_max]) + _flow(height[i_max:][::-1])
        
# @lc code=end

